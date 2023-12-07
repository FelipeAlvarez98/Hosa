import { UserList } from "../components/UserList";
import { useEffect } from "react";

export function UserPage() {
  return (
    <div className="mt-4 mx-auto max-w-screen-2xl">
      <UserList />
    </div>
  );
}
