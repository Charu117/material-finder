from flask import request, jsonify
from app import app, get_db_connection
from app.models import Material, Object

@app.route('/materials', methods=['GET'])
def get_materials():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Materials")
            materials = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            results = [Material(**dict(zip(columns, material))).__dict__ for material in materials]
    finally:
        conn.close()
    return jsonify(results)

@app.route('/objects', methods=['GET'])
def get_objects():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Objects")
            objects = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            results = [Object(**dict(zip(columns, obj))).__dict__ for obj in objects]
    finally:
        conn.close()
    return jsonify(results)

@app.route('/objects/<name>', methods=['GET'])
def get_object_by_name(name):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Objects WHERE name=%s", (name,))
            obj = cur.fetchone()
            if obj:
                columns = [desc[0] for desc in cur.description]
                obj = Object(**dict(zip(columns, obj))).__dict__
                cur.execute("SELECT * FROM Materials WHERE transparency>=%s AND density<=%s AND stiffness>=%s",
                            (obj['min_transparency'], obj['max_density'], obj['min_stiffness']))
                materials = cur.fetchall()
                material_columns = [desc[0] for desc in cur.description]
                obj['suitable_materials'] = [Material(**dict(zip(material_columns, material))).__dict__ for material in materials]
                return jsonify(obj)
    finally:
        conn.close()
    return jsonify({'error': 'Object not found'}), 404