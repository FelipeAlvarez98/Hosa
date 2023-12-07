import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Divider from "./Divider";

export function UserCard({ user }) {
  const navigate = useNavigate();
  const [isHovered, setIsHovered] = useState(false);

  return (
    <>
      <tr
        className={`${
          isHovered ? "bg-orange-600 text-white" : "bg-slate-100 text-black"
        } hover:bg-orange-600 hover:cursor-pointer`}
        onClick={() => {
          navigate(`/Crear-Usuario/${user.idUsuario}`);
        }}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <td className="py-2 px-4 border-b">{user.idUsuario}</td>
        <td className="py-2 px-4 border-b">{user.rut}</td>
        <td className="py-2 px-4 border-b">{user.nombreUsuario}</td>
        <td className="py-2 px-4 border-b">{user.correo}</td>
        <td className="py-2 px-4 border-b">{user.direccion}</td>
        <td className="py-2 px-4 border-b">{user.region?.nombreRegion}</td>
        <td className="py-2 px-4 border-b">{user.comuna?.nombreComuna}</td>
        <td className="py-2 px-4 border-b">{user.plan?.nombrePlan}</td>
        <td className="py-2 px-4 border-b">{user.config?.nombreConfig}</td>
      </tr>
      <Divider />
    </>
  );
}
