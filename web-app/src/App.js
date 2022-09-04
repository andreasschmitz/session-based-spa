import { useEffect, useState } from "react";

import Router from "./components/Route.js";
import Header from "./components/Header.js";
import Login from "./pages/Login.js";
import Reminders from "./pages/Reminders.js";
import { getUserAccount } from "./services/api";
import { UserCtx } from "./contexts/user.js";

function App() {
  const [user, setUser] = useState(null);
  const value = { user, setUser };

  useEffect(() => {
    async function fetchData() {
      // Retrieve initial CSRF cookie
      const user = await getUserAccount();

      if (user) {
        setUser({
          firstName: user.first_name,
          lastName: user.last_name,
        });
      } else {
        setUser(null);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="px-4">
      <UserCtx.Provider value={value}>
        <Header />
        <main className="container mx-auto mb-16">
          <Router path="/login">
            <Login />
          </Router>
          <Router path="/">
            <Reminders />
          </Router>
        </main>
      </UserCtx.Provider>
    </div>
  );
}

export default App;
