class GustoAppPage:
    def __init__(self, page):
        self.page = page

    def get_csrf_token(self):
        csrf_token = self.page.evaluate(
            "() => document.querySelector('meta[name=\"csrf-token\"]')?.content || "
            "window.__csrfToken || window.csrfToken || null"
        )
        if csrf_token:
            return csrf_token

        for cookie in self.page.context.cookies():
            if cookie.get("name") in {"csrf_token", "XSRF-TOKEN", "_csrf", "csrf"}:
                return cookie.get("value")
        return None

    def get_role_id(self):
        try:
            self.page.wait_for_function(
                "() => window.__DASHBOARD_DATA__ && (window.__DASHBOARD_DATA__.role_id || window.__DASHBOARD_DATA__.user?.role_id)",
                timeout=5000,
            )
        except Exception:
            pass

        role_id = self.page.evaluate(
            "() => window.__DASHBOARD_DATA__?.role_id || "
            "window.__DASHBOARD_DATA__?.user?.role_id || null"
        )
        if role_id:
            return str(role_id)

        return self.page.evaluate(
            """() => {
                const scripts = Array.from(document.scripts);
                for (const script of scripts) {
                    const text = script.textContent || "";
                    if (!text.includes("__DASHBOARD_DATA__")) continue;
                    const match = text.match(/role_id\\\"?:\\\"?(\\d+)\\\"?/);
                    if (match) return match[1];
                }
                return null;
            }"""
        )
