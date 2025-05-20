from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def load_homepage(self):
        self.client.get("/pages/homepage.html", name="Homepage (static)")

    @task(2)
    def login_success(self):
        self.client.post(
            "/pages/login.html",
            {"user": "admin", "pass": "secret"},
            name="Login (success)",
        )

    @task(1)
    def login_fail(self):
        self.client.post(
            "/pages/login.html",
            {"user": "foo", "pass": "bar"},
            name="Login (fail)",
        )
