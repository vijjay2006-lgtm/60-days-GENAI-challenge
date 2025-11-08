import asyncio
from playwright.async_api import async_playwright

# Cricbuzz official final scorecard link
URL = "https://www.cricbuzz.com/live-cricket-scorecard/121681/indw-vs-rsaw-final-icc-womens-world-cup-2025"

async def scrape_scorecard():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("🌐 Opening Cricbuzz ICC Final scorecard...")
        await page.goto(URL, timeout=90000)

        # Wait until the scorecard tables are loaded
        await page.wait_for_selector(".cb-col.cb-col-100.cb-ltst-wgt-hdr", timeout=90000)

        # Extract team names
        team_names = await page.locator(".cb-col.cb-col-100.cb-scrd-hdr-rw").all_text_contents()
        print("\n🏏 MATCH TEAMS:")
        for t in team_names:
            print("➡️", t.strip())

        # Extract all batting scorecards (each table block)
        print("\n📋 BATTING SCORECARDS:\n")
        innings = await page.locator(".cb-col.cb-col-100.cb-ltst-wgt-hdr").all()
        for idx, inn in enumerate(innings):
            team_header = (await inn.locator(".cb-col.cb-col-100.cb-scrd-hdr-rw").all_text_contents())
            if team_header:
                print(f"\n{'='*50}\n🏏 {team_header[0].strip()}\n{'='*50}")

            rows = await inn.locator("table tbody tr").all_text_contents()
            for row in rows:
                if row.strip():
                    print(row.strip())

        # Extract the final result
        result = await page.locator(".cb-col.cb-col-100.cb-min-inf").text_content()
        print("\n✅ MATCH RESULT:", result.strip())

        await browser.close()


if __name__ == "__main__":
    asyncio.run(scrape_scorecard())

