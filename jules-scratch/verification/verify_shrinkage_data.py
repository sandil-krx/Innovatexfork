from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to the dashboard
        # Using a file path since the server is running on localhost,
        # but this is more reliable for the script.
        page.goto("file:///app/src/dashboard/simple_dashboard.html")

        # The API call is to localhost:5000, so we need to wait for it to complete.
        # A simple way to do this is to wait for a specific element to be populated.
        shrinkage_value_locator = page.locator("#inventory-shrinkage-value")

        # Wait for the shrinkage value to not be the default '--'
        expect(shrinkage_value_locator).not_to_have_text("--", timeout=10000)

        # Take a screenshot of the inventory section
        inventory_section = page.locator("#inventory-section")
        inventory_section.screenshot(path="jules-scratch/verification/verification.png")

        print("Screenshot saved to jules-scratch/verification/verification.png")

    except Exception as e:
        print(f"An error occurred: {e}")
        page.screenshot(path="jules-scratch/verification/error.png")

    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)