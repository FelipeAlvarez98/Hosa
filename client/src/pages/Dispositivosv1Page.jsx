import React, { useState, useEffect } from "react";
import {
  getAllDispositivosv1,
  getTipoDispositivos,
  getSectores,
  getDetallesDispo,
  createDispositivov1,
  getAllUsers,
  getTiposDispositivo,
  getIdsTiposDispositivo
} from "../api/dispositivos.api";

export function Dispositivosv1Page() {
  const [formData, setFormData] = useState({
    userId: "", // Aquí debes tener el ID del usuario asociado
    sectorName: "",
    deviceType: "",
    deviceId: "",
    activityType: "",
    startTime: "",
    endTime: "",
  });

  const [tipoDispositivos, setTipoDispositivos] = useState([]);
  const [sectores, setSectores] = useState([]);
  const [detallesDispo, setDetallesDispo] = useState([]);
  const [users, setUsers] = useState([]); // Estado para almacenar la lista de usuarios
  const [searchTerm, setSearchTerm] = useState(""); // Estado para la barra de búsqueda
  const [idsTiposDispositivo, setIdsTiposDispositivo] = useState([]);


  useEffect(() => {
    // Obtener la lista de usuarios
    getAllUsers()
      .then((response) => {
        console.log("Usuarios obtenidos:", response.data);
        setUsers(response.data);
      })
      .catch((error) => console.error("Error obteniendo usuarios:", error));

    // Obtener datos de tipoDispositivos
    getTipoDispositivos()
      .then((response) => setTipoDispositivos(response.data))
      .catch((error) =>
        console.error("Error obteniendo tipo de dispositivos:", error)
      );

    // Obtener datos de sectores
    getSectores()
      .then((response) => setSectores(response.data))
      .catch((error) => console.error("Error obteniendo sectores:", error));

    // Obtener datos de detallesDispo
    getDetallesDispo()
      .then((response) => setDetallesDispo(response.data))
      .catch((error) =>
        console.error("Error obteniendo detallesdispo:", error)
      );

      getTiposDispositivo()
      .then((response) => setTipoDispositivos(response))
      .catch((error) => console.error("Error obteniendo tipo de dispositivos:", error));

    // Obtener IDs de tipos de dispositivo
    getIdsTiposDispositivo()
      .then((response) => setIdsTiposDispositivo(response))
      .catch((error) => console.error("Error obteniendo IDs de tipos de dispositivo:", error));

  }, []);

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Crea un objeto con los datos a enviar a la API
      const dataToSend = {
        userId: formData.userId,
        sectorName: formData.sectorName,
        deviceType: formData.deviceType,
        deviceId: formData.deviceId,
        activityType: formData.activityType,
        startTime: formData.startTime,
        endTime: formData.endTime,
      };

      // Llama a la API para crear el dispositivo
      const response = await createDispositivov1(dataToSend);

      // Puedes manejar la respuesta de la API según tus necesidades
      console.log("Respuesta de la API:", response.data);

      // Puedes agregar lógica adicional después de enviar los datos, como redirigir a otra página o mostrar un mensaje de éxito.
    } catch (error) {
      console.error("Error al enviar los datos:", error);
      // Puedes agregar lógica adicional para manejar errores, como mostrar un mensaje de error al usuario.
    }
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div className="mt-4 mx-auto max-w-screen-2xl text-black">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 rounded-lg shadow-md"
      >
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Buscar por Nombre o RUT:
          </label>
          <input
            type="text"
            name="searchTerm"
            value={searchTerm}
            onChange={handleSearchChange}
            placeholder="Buscar usuario por nombre o RUT..."
            className="mt-1 p-2 w-full border rounded-md"
          />
          <select
            name="userId"
            value={formData.userId}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          >
            <option value="">Selecciona un usuario</option>
            {users
              .filter(
                (user) =>
                  user.nombreUsuario
                    .toLowerCase()
                    .includes(searchTerm.toLowerCase()) ||
                  user.rut.toLowerCase().includes(searchTerm.toLowerCase())
              )
              .map((user) => (
                <option key={user.id} value={user.id}>
                  {user.nombreUsuario} ({user.rut})
                </option>
              ))}
          </select>
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Nombre de Sector:
          </label>
          <input
            type="text"
            name="sectorName"
            value={formData.sectorName}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Tipo de Dispositivo:
          </label>
          <select
            name="deviceType"
            value={formData.deviceType}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          >
            <option value="">Selecciona un tipo de dispositivo</option>
            {tipoDispositivos.map((tipo) => (
              <option key={tipo.id} value={tipo.id}>
                {tipo.tiposdispositivo}
              </option>
            ))}
          </select>
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            ID del Dispositivo:
          </label>
          <input
            type="text"
            name="deviceId"
            value={formData.deviceId}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          />
        </div>

        {/* <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Tipo de Actividad:
          </label>
          Agrega la lógica para la lista desplegable de actividad aquí
          <select
            name="activityType"
            value={formData.activityType}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          >
            Opciones para la lista desplegable de actividad
          </select>
        </div> */}

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Hora de Encendido:
          </label>
          <input
            type="time"
            name="startTime"
            value={formData.startTime}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">
            Hora de Apagado:
          </label>
          <input
            type="time"
            name="endTime"
            value={formData.endTime}
            onChange={handleInputChange}
            className="mt-1 p-2 w-full border rounded-md"
          />
        </div>

        <div className="flex items-center justify-end">
          <button
            type="submit"
            className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-300"
          >
            Guardar
          </button>
        </div>
      </form>
    </div>
  );
}

export default Dispositivosv1Page;
