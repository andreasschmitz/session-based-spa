import { useEffect, useState } from "react";

export function goTo(href, title = "") {
  window.history.pushState({}, title, href);
  const e = new PopStateEvent("popstate");
  window.dispatchEvent(e);
}

const Route = ({ path, children }) => {
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    const onLocationChange = () => {
      setCurrentPath(window.location.pathname);
    };

    window.addEventListener("popstate", onLocationChange);

    return () => {
      window.removeEventListener("popstate", onLocationChange);
    };
  }, []);

  return currentPath === path ? children : null;
};

export default Route;
