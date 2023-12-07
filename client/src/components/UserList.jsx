import React from "react";
import { useEffect, useState } from "react";
import { getAllUsers } from "../api/users.api";
import { getRegionDetails } from "../api/regiones.api";
import { getComunaDetails } from "../api/comunas.api";
import { getPlanDetails } from "../api/planes.api";
import { getConfigDetails } from "../api/usuarioConfig.api";
import { UserCard } from "./UserCard";

export function UserList() {
  const [users, setUsers] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    async function loadUsers() {
      try {
        const response = await getAllUsers();
        const usersWithDetails = await Promise.all(
          response.data.map(async (user) => {
            let comunaDetails = null;
            let regionDetails = null;

            // Verifica si idComuna está definido y no es null
            if (user.idComuna !== undefined && user.idComuna !== null) {
              const comunaResponse = await getComunaDetails(user.idComuna);
              comunaDetails = comunaResponse.data;
            }

            // Verifica si idRegion está definido y no es null
            if (user.idRegion !== undefined && user.idRegion !== null) {
              const regionResponse = await getRegionDetails(user.idRegion);
              regionDetails = regionResponse.data;
            }

            const planResponse = await getPlanDetails(user.idPlan);
            const configResponse = await getConfigDetails(user.idConfigUsuario);

            return {
              ...user,
              comuna: comunaDetails,
              region: regionDetails,
              plan: planResponse.data,
              config: configResponse.data,
            };
          })
        );

        setUsers(usersWithDetails);
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    }

    loadUsers();
  }, []);

  const filteredUsers = users.filter((user) =>
    user.rut.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="mt-4">
      <input
        type="text"
        placeholder="Buscar por Rut"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="p-2 mb-4 text-black rounded-lg ml-1"
      />
      <div className="overflow-x-auto ml-1 rounded-lg mx-auto">
        <table className="min-w-full bg-white border rounded">
          <thead className="bg-gray-100 text-black">
            <tr>
              <th>ID Usuario</th>
              <th>Rut</th>
              <th>Nombre Usuario</th>
              <th>Correo</th>
              <th>Dirección</th>
              <th>Región</th>
              <th>Comuna</th>
              <th>Plan</th>
              <th>Configuración</th>
            </tr>
          </thead>
          <tbody>
            {filteredUsers.map((user) => (
              <UserCard key={user.idUsuario} user={user} />
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default UserList;
