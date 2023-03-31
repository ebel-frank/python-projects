import sys
from ruamel.yaml import YAML


def create_a_node(output=sys.stdout):
    yaml = YAML()
    service = {
        "tosca_definitions_version": "tosca_simple_yaml_1_3",
        "relationship_types": {
            "basicrelationship": {
                "derived_from": "tosca.relationships.Root"
            }
        },
        "topology_template": {
            "node_templates": {
                "knowledge_base": {
                    "type": "tosca.nodes.SoftwareComponent",
                    "requirements": [{
                        "export": {
                            "node": "knowledge_base",
                            "relationship": "exports"
                        }}, {
                        "import": {
                            "node": "knowledge_base",
                            "relationship": "imports"
                        }
                    }
                    ]
                },
                "knowledge_base_manager": {
                    "type": "tosca.nodes.SoftwareComponent",
                    "requirements": [{
                        "export": {
                            "node": "knowledge_base",
                            "relationship": "exports"
                        }}, {
                        "optimize": {
                            "node": "knowledge_base",
                            "relationship": "optimizes"
                        }}
                    ]
                },
                "AN_Orchestrator": {
                    "type": "tosca.nodes.Compute",
                    "requirements": [{
                        "refer": {
                            "node": "knowledge_base",
                            "relationship": "refersTo"
                        }}, {
                        "generates_Tosca": {
                            "node": "Auto_Controller_Generator",
                            "relationship": "generates"
                        }}
                    ]
                },
                "Auto_Controller_Generator": {
                    "type": "tosca.nodes.SoftwareComponent",
                    "requirements": [
                        {"dependency": "ML_pipeline"}
                    ]
                },
                "OpenCN": {
                    "type": "tosca.nodes.SoftwareComponent",
                },
                "ML_pipeline": {
                    "type": "tosca.nodes.SoftwareComponent",
                },
                "Human_operator": {
                    "type": "tosca.nodes.SoftwareComponent",
                },
            },
            "relationship_templates": {
                "refersTo": {
                    "type": "basicrelationship"
                },
                "optimizes": {
                    "type": "basicrelationship"
                },
                "exports": {
                    "type": "basicrelationship"
                },
                "stores": {
                    "type": "basicrelationship"
                },
                "recommends": {
                    "type": "basicrelationship"
                },
                "imports": {
                    "type": "basicrelationship"
                },
                "reads": {
                    "type": "basicrelationship"
                },
                "monitors": {
                    "type": "basicrelationship"
                },
                "inputs": {
                    "type": "basicrelationship"
                },
                "generates": {
                    "type": "basicrelationship"
                },
            },
        }
    }
    print(service)
    yaml.dump(service, output)


def special_node():
    actors = ['AN Orchestrator', 'Auto controller generator', 'Human operator', 'Knowledge Base', 'Knowledge Base Manager', 'ML Pipeline', 'OpenCN', 'tosca format', 'x', 'controllers', 'reports', 'use case desc']
    m_actors = [actor for actor in actors if actor[0].isupper()]
    relation_test = [['export', 'Knowledge Base'], ['import', 'Knowledge Base']]
    relation = set({}) # This will be unique
    service = {
        "version": "1_3",
        "types": {
            "basicrelationship": {
                "derived": "Root"
            }
        },
        "topology_template": {
            "node_templates": {},
            "relationship_templates": {}
        }
    }

    for i in m_actors:
        service["topology_template"]["node_templates"].update(
            {i: {"type": "tosca.nodes.SoftwareComponent", "requirements": []}})
        service["topology_template"]["node_templates"][i].update({"requirements": []})
        # get relationship
        for j in relation_test:
            service["topology_template"]["node_templates"][i]["requirements"].append({j[0]: {
                "node": j[1], "relationship": j[0]
            }})
            relation.add(j[0])

    # update the topology_template -> relationship_template section
    # for i in relation:
    #     service["topology_template"]["relationship_templates"].update({i: {"type":"basicrelationship"}})
    print(service)
    print(relation)


def get_a_node(inputPath):
    yaml = YAML(typ='safe')
    with open(inputPath, 'r') as fp:
        data = dict(yaml.load(fp))
        print(data)


if __name__ == '__main__':
    output = open("testing.yaml", 'w')
    # get_a_node("testing.yaml")
    create_a_node(output)
    # special_node()
