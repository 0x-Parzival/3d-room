import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        page.on("pageerror", lambda exc: print(f"PAGE ERROR: {exc}"))

        await page.goto("http://localhost:8000/preview.html")

        # Wait for room model to load
        await asyncio.sleep(10)
        await page.screenshot(path="screenshot_room.png")
        print("Took screenshot_room.png")

        # Load kitchen model
        await page.click("text=View Kitchen")
        await asyncio.sleep(10)
        await page.screenshot(path="screenshot_kitchen.png")
        print("Took screenshot_kitchen.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
