import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="flex justify-between py-3 bg-orange-300 p-2 items-center rounded-lg">
      <Link to={"/backoffice"}>
        <div className="flex flex-row">
          <img src="/src/img/icon-hosa.png" alt="Logo" className="h-10 w-10" />
          <h1 className="font-bold text-3xl">BackOffice App</h1>
        </div>
      </Link>
      <ul className="flex flex-row gap-3">
        <Link to="/usuario">Usuarios</Link>
        <Link to="/crear-usuario">Crear Usuario</Link>
        <Link to="/dispositivosv1">Dispositivos</Link>
        <Link to="/ventas">Ventas</Link>
      </ul>
    </div>
  );
}
