class ElectricityPricingModel:
    def __init__(self):
        self.energy_sources = {}

    def add_energy_source(self, name, price_per_mwh, capacity_mwh):
        """
        Adds an energy source to the model.
        
        :param name: Name of the energy source (e.g., 'solar', 'wind').
        :param price_per_mwh: Price per MWh of the energy source.
        :param capacity_mwh: Amount of electricity (in MWh) the energy source is expected to provide.
        """
        self.energy_sources[name] = {'price_per_mwh': price_per_mwh, 'capacity_mwh': capacity_mwh}

    def calculate_market_price(self, demand_mwh):
        """
        Calculates the market price based on the highest-priced energy source that meets the demand.
        
        :param demand_mwh: Total electricity demand in MWh.
        :return: The market clearing price per MWh.
        """
        sorted_sources = sorted(self.energy_sources.items(), key=lambda x: x[1]['price_per_mwh'])
        
        total_supplied = 0
        price_setter = None
        marginal_price = 0
        
        for source, details in sorted_sources:
            if total_supplied + details['capacity_mwh'] >= demand_mwh:
                marginal_price = details['price_per_mwh']
                price_setter = source
                break
            total_supplied += details['capacity_mwh']
        
        
        return price_setter, marginal_price

# EXAMPLE
pricing_model = ElectricityPricingModel()
pricing_model.add_energy_source('solar', -50, 3000)
pricing_model.add_energy_source('wind', -40, 3000)
pricing_model.add_energy_source('geothermal', -30, 3000)
pricing_model.add_energy_source('lumbar', -20, 3000)
pricing_model.add_energy_source('hydro', 0, 3000)
pricing_model.add_energy_source('nuclear', 5, 3000)
pricing_model.add_energy_source('coal', 10, 3000)
pricing_model.add_energy_source('natural_gas', 20, 3000)
pricing_model.add_energy_source('oil', 25, 3000)
pricing_model.add_energy_source('jet_fuel', 35, 3000)
pricing_model.add_energy_source('refined_products', 45, 3000)


demand_mwh = 18001
price_setter, market_price = pricing_model.calculate_market_price(demand_mwh)
print(f"The market clearing price is: ${market_price} per MWh")
print(f"The price-setting energy source is: {price_setter}")
