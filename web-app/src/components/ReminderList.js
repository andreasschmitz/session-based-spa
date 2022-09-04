import { useState, useEffect, useContext } from "react";

import { UserCtx } from "../contexts/user";
import useIsMounted from "../hooks/useIsMounted";
import { getReminders } from "../services/api";

const ReminderList = () => {
  const { user } = useContext(UserCtx);
  const isMounted = useIsMounted();

  const [reminders, setReminders] = useState([]);
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    async function getData() {
      if (user === null) {
        return;
      }

      try {
        const response = await getReminders();
        isMounted.current && setReminders(response.data);
      } catch (error) {
        isMounted.current && setHasError(true);
        return;
      }
    }
    getData();
  }, [user]); // eslint-disable-line

  if (hasError) {
    return <div>Error retrieving reminders</div>;
  }

  if (user === null) {
    return <div>You need to log in to see the reminders.</div>;
  }

  return (
    <>
      {reminders.map((entry) => {
        return (
          <ul className="list-disc list-inside" key={entry.id}>
            <li className="flex justify-between max-w-md mb-6 p-4 bg-white shadow-lg ring-1 ring-black/5 rounded-md">
              <p>
                <span className="block font-bold">{entry.title}</span>
                <span className="text-zinc-700">{entry.note}</span>
              </p>
              <div className="ml-4">
                <input type="checkbox" checked={entry.done} disabled />
              </div>
            </li>
          </ul>
        );
      })}
    </>
  );
};

export default ReminderList;
