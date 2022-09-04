import { createContext } from "react";

export const UserCtx = createContext({
  user: null,
  setUser: (user) => {},
});
