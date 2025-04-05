from src.driver.driver_factory import create_driver

def before_scenario(context, scenario):
    print(f"\n[Setup] Starting scenario: {scenario.name}")
    context.driver = create_driver()

def after_scenario(context, scenario):
    print(f"[Teardown] Ending scenario: {scenario.name}")
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
