import React, { useContext } from "react";

import { UserCtx } from "../contexts/user";
import { logout } from "../services/api";

import Link from "./Link";
import { goTo } from "./Route";

const Header = () => {
  const { user, setUser } = useContext(UserCtx);

  async function logoutHandler(event) {
    await logout();
    setUser(null);
    goTo("/login", "Login");
  }

  return (
    <header className="container mx-auto my-8">
      <div className="flex justify-between">
        <Link href="/" className="font-bold">
          Reminders
        </Link>
        <div>
          {user === null ? (
            <Link href="/login" className="font-bold">
              Login
            </Link>
          ) : (
            <div>
              {`Welcome, ${user.firstName} (`}
              <button className="font-bold" onClick={logoutHandler}>
                Logout
              </button>
              {")"}
            </div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;
