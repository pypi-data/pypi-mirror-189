#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
EXPOsan: Exposition of sanitation and resource recovery systems

This module is developed by:

    Jianan Feng <jiananf2@illinois.edu>

    Yalin Li <mailto.yalin.li@gmail.com>
    
This module is under the University of Illinois/NCSA Open Source License.
Please refer to https://github.com/QSD-Group/EXPOsan/blob/main/LICENSE.txt
for license details.

References:

(1) Jones, S. B.; Zhu, Y.; Anderson, D. B.; Hallen, R. T.; Elliott, D. C.; 
    Schmidt, A. J.; Albrecht, K. O.; Hart, T. R.; Butcher, M. G.; Drennan, C.; 
    Snowden-Swan, L. J.; Davis, R.; Kinchin, C. 
    Process Design and Economics for the Conversion of Algal Biomass to
    Hydrocarbons: Whole Algae Hydrothermal Liquefaction and Upgrading;
    PNNL--23227, 1126336; 2014; https://doi.org/10.2172/1126336.
'''

from biosteam import TEA
import numpy as np, pandas as pd, thermosteam as tmo, biosteam as bst

__all__ = ('HTL_TEA', 'create_tea',)

class CAPEXTableBuilder:
    __slots__ = ('index', 'data')
    
    def __init__(self):
        self.index = []
        self.data =[]
    
    def entry(self, index: str, cost: list, notes: str = '-'):
        self.index.append(index)
        self.data.append([notes, *cost])

    @property
    def total_costs(self):
        N = len(self.data[0])
        return [sum([i[index] for i in self.data]) for index in range(1, N)]
    
    def table(self, names):
        return pd.DataFrame(self.data, 
                            index=self.index,
                            columns=('Notes', *[i + ' [MM$]' for i in names])
        )


class HTL_TEA(TEA):
    
    __slots__ = ('OSBL_units', 'warehouse', 'site_development',
                 'additional_piping', 'proratable_costs', 'field_expenses',
                 'construction', 'contingency', 'other_indirect_costs', 
                 'labor_cost', 'labor_burden', 'property_insurance',
                 'maintenance', '_ISBL_DPI_cached', '_FCI_cached',
                 '_utility_cost_cached', '_steam_power_depreciation',
                 '_steam_power_depreciation_array',
                 'boiler_turbogenerator')
    
    def __init__(self, system, IRR, duration, depreciation, income_tax,
                 operating_days, lang_factor, construction_schedule,
                 startup_months, startup_FOCfrac, startup_VOCfrac,
                 startup_salesfrac, WC_over_FCI,  finance_interest,
                 finance_years, finance_fraction, OSBL_units, warehouse,
                 site_development, additional_piping, proratable_costs,
                 field_expenses, construction, contingency,
                 other_indirect_costs, labor_cost, labor_burden,
                 property_insurance, maintenance, steam_power_depreciation,
                 boiler_turbogenerator):
        super().__init__(system, IRR, duration, depreciation, income_tax,
                         operating_days, lang_factor, construction_schedule,
                         startup_months, startup_FOCfrac, startup_VOCfrac,
                         startup_salesfrac, WC_over_FCI,  finance_interest,
                         finance_years, finance_fraction)
        self.OSBL_units = OSBL_units
        self.warehouse = warehouse
        self.site_development = site_development
        self.additional_piping = additional_piping
        self.proratable_costs = proratable_costs
        self.field_expenses = field_expenses
        self.construction = construction
        self.contingency = contingency
        self.other_indirect_costs = other_indirect_costs
        self.labor_cost = labor_cost
        self.labor_burden = labor_burden
        self.property_insurance = property_insurance
        self.maintenance = maintenance
        self.steam_power_depreciation = steam_power_depreciation
        self.boiler_turbogenerator = boiler_turbogenerator
        
    @property
    def steam_power_depreciation(self):
        """[str] 'MACRS' + number of years (e.g. 'MACRS7')."""
        return self._steam_power_depreciation
    @steam_power_depreciation.setter
    def steam_power_depreciation(self, depreciation):
        self._steam_power_depreciation_array = self._depreciation_array_from_key(
            self._depreciation_key_from_name(depreciation)
        )
        self._steam_power_depreciation = depreciation
    
    @property
    def ISBL_installed_equipment_cost(self):
        return self._ISBL_DPI(self.DPI)
    
    @property
    def OSBL_installed_equipment_cost(self):
        if self.lang_factor:
            raise NotImplementedError('lang factor cannot yet be used')
        elif isinstance(self.system, bst.AgileSystem):
            unit_capital_costs = self.system.unit_capital_costs
            OSBL_units = self.OSBL_units
            return sum([unit_capital_costs[i].installed_cost for i in OSBL_units])
        else:
            return sum([i.installed_cost for i in self.OSBL_units])
    
    def _fill_depreciation_array(self, D, start, years, TDC):
        depreciation_array = self._get_depreciation_array()
        N_depreciation_years = depreciation_array.size
        if N_depreciation_years > years:
            raise RuntimeError('depreciation schedule is longer than plant lifetime')
        system = self.system
        BT = self.boiler_turbogenerator
        if BT is None:
            D[start:start + N_depreciation_years] = TDC * depreciation_array
        else:
            if isinstance(system, bst.AgileSystem): BT = system.unit_capital_costs[BT]
            BT_TDC = BT.installed_cost 
            D[start:start + N_depreciation_years] = (TDC - BT_TDC) * depreciation_array
            
            depreciation_array = self._steam_power_depreciation_array
            N_depreciation_years = depreciation_array.size
            if N_depreciation_years > years:
                raise RuntimeError('steam power depreciation schedule is longer than plant lifetime')
            D[start:start + N_depreciation_years] += BT_TDC * depreciation_array
    
    def _ISBL_DPI(self, installed_equipment_cost):
        """Direct permanent investment of units inside battery limits."""
        if self.lang_factor:
            raise NotImplementedError('lang factor cannot yet be used')
        else:
            self._ISBL_DPI_cached = installed_equipment_cost - self.OSBL_installed_equipment_cost
        return self._ISBL_DPI_cached
        
    def _DPI(self, installed_equipment_cost):
        factors = self.warehouse + self.site_development + self.additional_piping
        return installed_equipment_cost + self._ISBL_DPI(installed_equipment_cost) * factors
    
    def _indirect_costs(self, TDC):
        return TDC*(self.proratable_costs + self.field_expenses
                    + self.construction + self.contingency
                    + self.other_indirect_costs)
    
    def _FCI(self, TDC):
        self._FCI_cached = FCI = TDC + self._indirect_costs(TDC)
        return FCI
    
    def _FOC(self, FCI):
        return (FCI * self.property_insurance
                + self._ISBL_DPI_cached * self.maintenance
                + self.labor_cost * (1 + self.labor_burden))


def create_tea(sys, OSBL_units=None, cls=None):
    if OSBL_units is None: OSBL_units = bst.get_OSBL(sys.cost_units)
    try:
        BT = tmo.utils.get_instance(OSBL_units, (bst.BoilerTurbogenerator, bst.Boiler))
    except:
        BT = None
    if cls is None: cls = HTL_TEA
    tea = cls(
        system=sys, 
        IRR=0.10, # Jones
        duration=(2022, 2052), # Jones
        depreciation='MACRS7', # Jones
        income_tax=0.35, # Jones
        operating_days=330, # Jones
        lang_factor=None, # related to expansion, not needed here
        construction_schedule=(0.08, 0.60, 0.32), # Jones
        startup_months=6, # Jones
        startup_FOCfrac=1, # Davis NREL 2018
        startup_salesfrac=0.5, # Davis NREL 2018
        startup_VOCfrac=0.75, # Davis NREL 2018
        WC_over_FCI=0.05, # Jones
        finance_interest=0.08, # Jones
        finance_years=10, # Jones
        finance_fraction=0.6, # debt: Jones
        OSBL_units=OSBL_units,
        warehouse=0.04, # NREL 2013
        site_development=0.09, # NREL 2013
        additional_piping=0.045, # NREL 2013
        proratable_costs=0.10, # NREL 2013
        field_expenses=0.10, # NREL 2013
        construction=0.20, # NREL 2013
        contingency=0.10, # NREL 2013
        other_indirect_costs=0.10, # NREL 2013
        labor_cost=2.5e6, # use default value
        labor_burden=0.90, # Jones and Davis
        property_insurance=0.007, # Jones & NREL 2013
        maintenance=0.03, # Jones & NREL 2013
        steam_power_depreciation='MACRS20',
        boiler_turbogenerator=BT)
    return tea

def capex_table(teas, names=None):
    if isinstance(teas, bst.TEA): teas = [teas]
    capex = CAPEXTableBuilder()
    tea, *_ = teas
    ISBL_installed_equipment_costs = np.array([i.ISBL_installed_equipment_cost / 1e6 for i in teas])
    OSBL_installed_equipment_costs = np.array([i.OSBL_installed_equipment_cost / 1e6 for i in teas])
    capex.entry('ISBL installed equipment cost', ISBL_installed_equipment_costs)
    capex.entry('OSBL installed equipment cost', OSBL_installed_equipment_costs)
    ISBL_factor_entry = lambda name, value: capex.entry(name, ISBL_installed_equipment_costs * value, f"{value:.1%} of ISBL")
    ISBL_factor_entry('Warehouse', tea.warehouse)
    ISBL_factor_entry('Site development', tea.site_development)
    ISBL_factor_entry('Additional piping', tea.additional_piping)
    TDC = np.array(capex.total_costs)
    capex.entry('Total direct cost (TDC)', TDC)
    TDC_factor_entry = lambda name, value: capex.entry(name, TDC * value, f"{value:.1%} of TDC")
    TDC_factor_entry('Proratable costs', tea.proratable_costs)
    TDC_factor_entry('Field expenses', tea.field_expenses)
    TDC_factor_entry('Construction', tea.construction)
    TDC_factor_entry('Contingency', tea.contingency)
    TDC_factor_entry('Other indirect costs (start-up, permits, etc.)', tea.other_indirect_costs)
    TIC = np.array(capex.total_costs) - 2 * TDC
    capex.entry('Total indirect cost', TIC)
    FCI = TDC + TIC
    capex.entry('Fixed capital investment (FCI)', FCI)
    working_capital = FCI * tea.WC_over_FCI
    capex.entry('Working capital', working_capital, f"{tea.WC_over_FCI:.1%} of FCI")
    TCI = FCI + working_capital
    capex.entry('Total capital investment (TCI)', TCI)
    if names is None: names = [i.system.ID for i in teas]
    names = [i for i in names]
    return capex.table(names)

voc_table = bst.report.voc_table

def foc_table(teas, names=None):
    if isinstance(teas, bst.TEA): teas = [teas]
    tea, *_ = teas
    foc = bst.report.FOCTableBuilder()
    ISBL = np.array([i.ISBL_installed_equipment_cost / 1e6 for i in teas])
    labor_cost = np.array([i.labor_cost / 1e6 for i in teas])
    foc.entry('Labor salary', labor_cost)
    foc.entry('Labor burden', tea.labor_burden * labor_cost, '90% of labor salary')
    foc.entry('Maintenance', tea.maintenance * ISBL, f'{tea.maintenance:.1%} of ISBL')
    foc.entry('Property insurance', tea.property_insurance * ISBL, f'{tea.property_insurance:.1%} of ISBL')
    if names is None: names = [i.system.ID for i in teas]
    names = [i + ' MM$/yr' for i in names]
    return foc.table(names)