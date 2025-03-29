from typing import Dict, List
import json
import os
from datetime import datetime

class CypherGenerator:
    def convert_entities_to_cypher(self, entities: List[Dict]) -> str:
        queries = []
        for entity in entities:
            label = entity.get("type", "Entity").replace(" ", "")
            name = entity["name"].replace('"', '\\"')
            queries.append(
                f'CREATE (n:{label} {{ name: "{name}" }})'
            )
        return ';\n'.join(queries)

    def convert_relationships_to_cypher(self, relationships: List[Dict]) -> str:
        queries = []
        for rel in relationships:
            source = rel["source"].replace('"', '\\"')
            target = rel["target"].replace('"', '\\"')
            rel_type = rel["relationship"].replace(" ", "_").upper()
            queries.append(f'''
MATCH (e1 {{name: "{source}"}})
MATCH (e2 {{name: "{target}"}})
MERGE (e1)-[:{rel_type}]->(e2)''')
        return ';\n'.join(queries)

    def save_cypher_to_file(self, final_query: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"neo4j_query_{timestamp}.cypher"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(final_query)
        print(f"✅ Cypher query saved to: {filename}")

    def process_json(self, json_data):
        if isinstance(json_data, str):
            try:
                data = json.loads(json_data)
            except json.JSONDecodeError as e:
                raise Exception(f"Error parsing JSON: {e}")
        else:
            data = json_data

        all_queries = []

        if "entities" in data:
            entity_query = self.convert_entities_to_cypher(data["entities"])
            all_queries.append(entity_query)

        if "relationships" in data:
            rel_query = self.convert_relationships_to_cypher(data["relationships"])
            all_queries.append(rel_query)

        final_query = ';\n'.join(all_queries) + ';'
        self.save_cypher_to_file(final_query)


def load_json_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception(f"❌ File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise Exception(f"❌ Invalid JSON: {str(e)}")
    except Exception as e:
        raise Exception(f"❌ Error reading file: {str(e)}")


def main():
    try:
        file_name = input("📄 Enter the JSON filename to convert (e.g., kb_results1.json): ").strip()
        file_path = os.path.join(os.getcwd(), file_name)

        # Load and process the JSON
        json_data = load_json_file(file_path)
        generator = CypherGenerator()
        generator.process_json(json_data)

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
