from tools.class_source import get_class_source, get_class_source_definition
from tools.where_used_list import get_where_used_list, get_where_used_definition
from tools.function_source import get_function_source, get_function_source_definition
from tools.function_group_source import get_function_group_source, get_function_group_source_definition
from tools.include_source import get_include_source, get_include_source_definition
from tools.interface_source import  get_interface_source, get_interface_source_definition
from tools.package_structure import  get_package_structure, get_package_structure_definition
from tools.program_source import get_program_source, get_program_source_definition
from tools.structure_source import get_structure_source, get_structure_source_definition
from tools.table_source import get_table_source, get_table_source_definition
from tools.transaction_properties import get_transaction_properties, get_transaction_properties_definition
from tools.type_info import get_type_info, get_type_info_definition
from tools.search_objects import get_search_objects, get_search_objects_definition
from tools.usage_references import get_usage_references, get_usage_references_definition

# All function-calling schemas for Gemini
tool_definitions = [
    get_class_source_definition,
    get_function_source_definition,
    get_function_group_source_definition,
    get_include_source_definition,
    get_interface_source_definition,
    get_package_structure_definition,
    get_program_source_definition,
    get_structure_source_definition,
    get_table_source_definition,
    get_transaction_properties_definition,
    get_type_info_definition,
    get_search_objects_definition,
    get_usage_references_definition
]

# Mapping name → function for invocation
tool_functions = {
    "get_class_source":     get_class_source,
    #"get_where_used_list":  get_where_used_list,
    "get_function_source": get_function_source,
    "get_function_group_source": get_function_group_source,
    "get_include_source": get_include_source,
    "get_interface_source": get_interface_source,
    "get_package_structure": get_package_structure,
    "get_program_source": get_program_source,
    "get_structure_source": get_structure_source,
    "get_table_source": get_table_source,
    "get_transaction_properties": get_transaction_properties,
    "get_type_info": get_type_info,
    "get_search_objects": get_search_objects,
    "get_usage_references": get_usage_references
}