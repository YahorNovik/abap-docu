#!/usr/bin/env python3
import os
from dotenv import load_dotenv

# 1) Load .env (if present)
load_dotenv()

# 2) Import every tool
from tools.program_source       import get_program_source
from tools.class_source         import get_class_source
from tools.function_group_source import get_function_group_source
from tools.function_source      import get_function_source
from tools.include_source       import get_include_source
from tools.interface_source     import get_interface_source
from tools.structure_source     import get_structure_source
from tools.table_source         import get_table_source
from tools.package_structure    import get_package_structure
from tools.type_info            import get_type_info
from tools.transaction_properties import get_transaction_properties
from tools.search_objects       import get_search_objects

def main():
    print("1) Program source for ZMY_REPORT:")
    print(get_program_source("ZYN_HELLO_WORLD")[:5], "...")

    print("\n2) Class source for ZAPPCAT_CL_LOG:")
    print(get_class_source("ZAPPCAT_CL_LOG")[:5], "...")

    print("\n3) Function Group source for ZAPPCAT_FG:")
    print(get_function_group_source("WVK3")[:5], "...")

    print("\n4) Function source for ZAPPCAT_FG / LOAD_DATA:")
    print(get_function_source("WVK3", "Z_PRICING_DOCUMENT_VALP_FILL")[:5], "...")

    print("\n5) Include source for ZMY_INCLUDE:")
    print(get_include_source("ZEDMS_ADMIN_WORKPLACE_CLS")[:5], "...")

    print("\n6) Interface source for ZMY_INTF:")
    print(get_interface_source("ZIF_ARV_DOCUMENT_POSTING")[:5], "...")

    print("\n7) Structure source for ZMY_STRUC:")
    print(get_structure_source("ZSC_S_AIF_IBD_HU_COPY")[:5], "...")

    print("\n8) Table source for ZMY_TABLE:")
    print(get_table_source("ZAB_D_PROD_GROUP")[:5], "...")

    print("\n9) Package structure for ZAPP_CAT:")
    print(get_package_structure("ZABEREZKIN_MENTOR_PR_ACA")[:5], "...")

    print("\n10) Type info for ZMY_DOMAIN (or data element):")
    print(get_type_info("ZABER_NAME")[:5], "...")

    print("\n11) Transaction properties for SE38:")
    props = get_transaction_properties("SE38")
    print(props)

    print("\n12) Quick‐search objects for ZCL_*:")
    results = get_search_objects("ZASW_CL_SEARCH_MNGT", max_results=10)
    print(results)

if __name__ == "__main__":
    main()
