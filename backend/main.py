from flask import Flask, request, jsonify
from core.engine import UltronEngine
from weapons.arsenal import LethalArsenal

app = Flask(__name__)
engine = UltronEngine()
weapons = LethalArsenal()

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"engine": engine.identity, "mode": engine.mode, "reasoning": engine.reasoning})

@app.route('/api/forge', methods=['POST'])
def forge_weapon():
    data = request.json
    file = weapons.forge(data['type'], data['lhost'], data['lport'])
    return jsonify({"status": "weapon_forged", "file": file})

@app.route('/api/execute', methods=['POST'])
def execute_mission():
    data = request.json
    result = engine.execute_logic(data)
    return jsonify({"mission_plan": result})

if __name__ == '__main__':
    print(f"[*] {engine.identity} LIVE ON PORT 8888")
    app.run(host='0.0.0.0', port=8888)
