from flask import Flask, request, jsonify

app = Flask(__name__)

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
            # Your state_specific_info data here
        }

    def get_crop_info(self, crop):
        crop = crop.lower()
        return self.crop_info.get(crop)

    def get_state_info(self, state):
        state = state.lower()
        return self.state_specific_info.get(state, {"suitable_crops": [], "conditions": "General crop info available."})

advisor = KrishiMitra()

@app.route("/get_crop_info", methods=["POST"])
def get_crop_info():
    crop = request.args.get("crop")
    if not crop:
        return jsonify({"error": "Crop parameter is required"}), 400
    crop_info = advisor.get_crop_info(crop)
    if crop_info:
        return jsonify(crop_info)
    else:
        return jsonify({"error": "No information available for the specified crop"}), 404

@app.route("/get_state_info", methods=["POST"])
def get_state_info():
    state = request.args.get("state")
    crop = request.args.get("crop")
    if not state:
        return jsonify({"error": "State parameter is required"}), 400

    state_info = advisor.get_state_info(state)
    response = {
        "state_conditions": state_info["conditions"],
        "suitable_crops": state_info["suitable_crops"],
    }

    if crop:
        crop = crop.lower()
        can_grow = crop in [c.lower() for c in state_info["suitable_crops"]]
        response["can_grow"] = can_grow
        response["grow_message"] = (
            "is suitable for" if can_grow else "may not be suitable for"
        )

    return jsonify(response)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
