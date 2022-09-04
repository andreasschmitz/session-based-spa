import { useState, useContext } from "react";

import { goTo } from "../components/Route";
import { UserCtx } from "../contexts/user";
import { login, getUserAccount } from "../services/api";

const Login = () => {
  const { setUser } = useContext(UserCtx);

  const [username, setUsername] = useState("user_1");
  const [password, setPassword] = useState("csrf1234");
  const [hasError, setHasError] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      await login(username, password);
      const user = await getUserAccount();
      const _user = {
        firstName: user.first_name,
        lastName: user.last_name,
      };
      setUser(_user);
    } catch (error) {
      setHasError(true);
      return;
    }

    goTo("/", "Reminders");
  };

  return (
    <form className="max-w-md mx-auto p-6" onSubmit={handleSubmit}>
      <div className="mb-4">
        <label className="block" htmlFor="username">
          Username:
        </label>
        <input
          className="w-full"
          id="username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          autoFocus
        />
      </div>
      <div className="mb-4">
        <label className="block" htmlFor="password">
          Password:
        </label>
        <input
          className="w-full"
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      {hasError && <div className="mt-6 mb-2 text-red-600">Log-in failed.</div>}

      <button
        className="w-full px-4 py-2 text-white no-underline rounded-md bg-zinc-700 hover:bg-zinc-800 active:bg-zinc-900 focus:outline-none focus:ring focus:ring-blue-300"
        type="submit"
      >
        Submit
      </button>
    </form>
  );
};

export default Login;
