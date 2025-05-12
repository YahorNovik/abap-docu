# test_usage_references.py

from tools.usage_references import get_usage_references

def test_for_object(object_type, object_name, **kwargs):
    print(f"\n=== {object_type.upper()}: {object_name} ===")
    try:
        refs = get_usage_references(
            object_type=object_type,
            object_name=object_name,
            **kwargs
        )
        print('Here are reefs')
        print(refs)
        print('Here are reefs')
        for r in refs:
            print(f" • {r['type']:10} {r['name']:30} {r['uri']}")
    except Exception as e:
        print(f"ERROR: {e}")

def main():
    # 1) Class
    test_for_object(
        "class",
        "ZAPPCAT_CL_LOG"
    )

    # 2) Program
    test_for_object(
        "program",
        "ZYN_HELLO_WORLD",
        start_position={"row": 1, "col": 0}
    )

    # 3) Include
    test_for_object(
        "include",
        "ZEDMS_ADMIN_WORKPLACE_CLS",
        start_position={"row": 1, "col": 0}
    )

    # 4) Interface
    test_for_object(
        "interface",
        "ZIF_ARV_DOCUMENT_POSTING"
    )

    # 5) Table
    test_for_object(
        "table",
        "ZAB_D_PROD_GROUP"
    )

    # 6) Structure
    test_for_object(
        "structure",
        "ZSC_S_AIF_IBD_HU_COPY"
    )

    # 7) Function Module
    test_for_object(
        "function_module",
        "CRM_ORDER_READ",
        function_group="CRM_ORDER_API"
    )

if __name__ == "__main__":
    main()
