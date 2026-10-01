import { defineConfig } from "@playwright/test";

// The acceptance test in design/tests, unchanged, against the built site on port 3000.
//   npm run build && npm run test:visual        (or BASE_URL=http://localhost:3000 npx playwright test)
export default defineConfig({
  testDir: "./design/tests",
  timeout: 120_000,
  workers: 4,
  reporter: [["list"]],
  webServer: {
    command: "npm run start -- -p 3000",
    url: "http://localhost:3000",
    reuseExistingServer: true,
    timeout: 120_000,
  },
});
