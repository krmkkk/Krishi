class KrishiMitra:
    def __init__(self):
        self.crop_info = {
            'wheat': {
                'soil_type': 'loamy or sandy',
                'weather': 'temperate climate with moderate rainfall',
                'temperature': '15-20°C',
                'fertilizer': 'Urea, DAP (Diammonium Phosphate)',
                'best_time': 'October to December for Rabi crop.',
            },
            'rice': {
                'soil_type': 'clay or loamy',
                'weather': 'tropical or subtropical with high humidity',
                'temperature': '20-35°C',
                'fertilizer': 'Urea, NPK (Nitrogen, Phosphorus, Potassium)',
                'best_time': 'June to September for Kharif crop.',
            },
            'barley': {
                'soil_type': 'well-drained, loamy',
                'weather': 'cool, dry conditions',
                'temperature': '12-20°C',
                'fertilizer': 'NPK and organic manure',
                'best_time': 'November to January for Rabi crop.',
            },
            'maize': {
                'soil_type': 'well-drained, loamy soil',
                'weather': 'warm, moist conditions',
                'temperature': '20-30°C',
                'fertilizer': 'Urea, NPK, and farmyard manure',
                'best_time': 'April to June for Kharif crop.',
            },
            'potato': {
                'soil_type': 'well-drained, sandy or loamy',
                'weather': 'cool climates, with good sunlight',
                'temperature': '15-20°C',
                'fertilizer': 'NPK and compost',
                'best_time': 'October to December for Rabi crop.',
            },
            'sugarcane': {
                'soil_type': 'alluvial or loamy',
                'weather': 'tropical with high rainfall',
                'temperature': '20-30°C',
                'fertilizer': 'NPK and farmyard manure',
                'best_time': 'February to April for planting.',
            },
            'tea': {
                'soil_type': 'acidic, well-drained',
                'weather': 'humid and tropical',
                'temperature': '15-30°C',
                'fertilizer': 'Organic manure and NPK',
                'best_time': 'March to June for planting.',
            },
            'cotton': {
                'soil_type': 'well-drained, loamy',
                'weather': 'hot and dry conditions',
                'temperature': '20-30°C',
                'fertilizer': 'NPK and vermicompost',
                'best_time': 'April to June for Kharif crop.',
            },
            'coffee': {
                'soil_type': 'well-drained, loamy',
                'weather': 'tropical, with rainfall',
                'temperature': '15-24°C',
                'fertilizer': 'Organic compost and NPK',
                'best_time': 'June to August for planting.',
            },
            'pulses': {
                'soil_type': 'well-drained, loamy',
                'weather': 'varies, but generally warm',
                'temperature': '15-30°C',
                'fertilizer': 'Organic manure and NPK',
                'best_time': 'June to August for Kharif crop.',
            },
            'millets': {
                'soil_type': 'sandy to loamy',
                'weather': 'dry conditions',
                'temperature': '20-30°C',
                'fertilizer': 'NPK and organic matter',
                'best_time': 'June to July for Kharif crop.',
            },
            'jute': {
                'soil_type': 'well-drained, alluvial',
                'weather': 'hot and humid',
                'temperature': '25-35°C',
                'fertilizer': 'NPK and organic manure',
                'best_time': 'April to June for planting.',
            }
        }

        self.state_specific_info = {
            'andhra pradesh': {'suitable_crops': ['rice', 'cotton', 'sugarcane'], 'conditions': 'Tropical climate, suitable for a variety of crops.'},
            'arunachal pradesh': {'suitable_crops': ['rice', 'millets'], 'conditions': 'Hilly terrain with moderate rainfall, best for rice and millets.'},
            'assam': {'suitable_crops': ['tea', 'rice', 'jute'], 'conditions': 'Humid climate, ideal for tea and rice cultivation.'},
            'bihar': {'suitable_crops': ['rice', 'maize', 'pulses'], 'conditions': 'Warm and humid, suitable for rice and pulses.'},
            'chhattisgarh': {'suitable_crops': ['rice', 'pulses'], 'conditions': 'Warm climate with adequate rainfall, great for rice.'},
            'goa': {'suitable_crops': ['rice', 'coconut'], 'conditions': 'Tropical coastal climate, suitable for rice and coconut.'},
            'gujarat': {'suitable_crops': ['cotton', 'groundnut'], 'conditions': 'Hot and dry, best for cotton and oilseeds.'},
            'haryana': {'suitable_crops': ['wheat', 'sugarcane'], 'conditions': 'Temperate climate, ideal for wheat and sugarcane.'},
            'himachal pradesh': {'suitable_crops': ['apple', 'potato'], 'conditions': 'Cool climate, best for fruits and vegetables.'},
            'jammu and kashmir': {'suitable_crops': ['rice', 'saffron'], 'conditions': 'Cold climate, suitable for specific crops like saffron.'},
            'jharkhand': {'suitable_crops': ['rice', 'pulses'], 'conditions': 'Moderate climate, suitable for rice and pulses.'},
            'karnataka': {'suitable_crops': ['coffee', 'cotton', 'rice'], 'conditions': 'Diverse climate, supports multiple crops.'},
            'kerala': {'suitable_crops': ['rice', 'tea', 'rubber'], 'conditions': 'High rainfall, ideal for rice and tea.'},
            'madhya pradesh': {'suitable_crops': ['wheat', 'pulses'], 'conditions': 'Varied climate, good for pulses and wheat.'},
            'maharashtra': {'suitable_crops': ['cotton', 'sugarcane'], 'conditions': 'Hot and dry, suitable for sugarcane and cotton.'},
            'manipur': {'suitable_crops': ['rice', 'vegetables'], 'conditions': 'Moderate climate, good for rice and local vegetables.'},
            'meghalaya': {'suitable_crops': ['rice', 'ginger'], 'conditions': 'High rainfall, suitable for rice and ginger.'},
            'mizoram': {'suitable_crops': ['rice', 'fruits'], 'conditions': 'Hilly terrain, best for rice and various fruits.'},
            'nagaland': {'suitable_crops': ['rice', 'millets'], 'conditions': 'Cool and humid, suitable for rice and millets.'},
            'odisha': {'suitable_crops': ['rice', 'pulses'], 'conditions': 'High rainfall, best for rice and pulses.'},
            'punjab': {'suitable_crops': ['wheat', 'rice'], 'conditions': 'Ideal for wheat and rice, well-irrigated.'},
            'rajasthan': {'suitable_crops': ['wheat', 'barley'], 'conditions': 'Arid conditions, best for drought-resistant crops.'},
            'sikkim': {'suitable_crops': ['cardamom', 'vegetables'], 'conditions': 'Cool climate, suitable for high-value crops.'},
            'tamil nadu': {'suitable_crops': ['rice', 'sugarcane'], 'conditions': 'Tropical climate, suitable for rice and sugarcane.'},
            'telangana': {'suitable_crops': ['rice', 'cotton'], 'conditions': 'Diverse agriculture, suitable for many crops.'},
            'uttar pradesh': {'suitable_crops': ['wheat', 'sugarcane'], 'conditions': 'Ideal for wheat and sugarcane.'},
            'uttarakhand': {'suitable_crops': ['fruits', 'vegetables'], 'conditions': 'Cool climate, suitable for various fruits and vegetables.'},
            'west bengal': {'suitable_crops': ['rice', 'jute', 'tea'], 'conditions': 'Humid, ideal for rice and jute.'},
        }

    def get_crop_info(self, crop):
        crop = crop.lower()
        return self.crop_info.get(crop)

    def get_state_info(self, state):
        state = state.lower()
        return self.state_specific_info.get(state, {"suitable_crops": [], "conditions": "General crop info available."})

def main():
    print("Welcome to KrishiMitra, your personal Chatbot!")
   
    advisor = KrishiMitra()

    while True:
        crop = input("\nEnter the crop you want to grow (or type 'exit' to quit): ")
        if crop.lower() == 'exit':
            print("Thank you for using Mitra! Goodbye!")
            break

        crop_info = advisor.get_crop_info(crop)
        if crop_info:
            print(f"\nInformation for {crop.capitalize()}:")
            for key, value in crop_info.items():
                print(f"{key.capitalize()}: {value}")

            state = input("\nWhich state in India do you live in? ")
            state_info = advisor.get_state_info(state)

            can_grow = crop.lower() in [c.lower() for c in state_info['suitable_crops']]
            grow_message = "is suitable for" if can_grow else "may not be suitable for"
            print(f"This crop {grow_message} {state.capitalize()} due to: {state_info['conditions']}")
        else:
            print("Sorry, I don't have information on that crop.")

if __name__ == "__main__":
    main()
