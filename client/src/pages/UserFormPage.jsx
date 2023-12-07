import React from "react";
import { useEffect } from "react";
import { useForm } from "react-hook-form";
import {
  createUsers,
  deleteUsers,
  updateUsers,
  getUser,
} from "../api/users.api";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-hot-toast";

export function UserFormPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    setValue,
  } = useForm();
  const navigate = useNavigate();
  const params = useParams();
  // console.log(params);

  const onSubmit = handleSubmit(async (data) => {
    // const res = await createUsers(data);
    // navigate("/BackOffice");
    if (params.idUsuario) {
      console.log(data);
      await updateUsers(params.idUsuario, data);
      toast.success("Usuario actualizado", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    } else {
      await createUsers(data);
      toast.success("Usuario Creado", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    }
    navigate("/Usuario");
  });

  useEffect(() => {
    async function loadUser() {
      if (params.idUsuario) {
        console.log("obteniendo datos");
        const res = await getUser(params.idUsuario);
        setValue("rut", res.data.rut);
        setValue("idUsuario", res.data.idUsuario);
        setValue("nombreUsuario", res.data.nombreUsuario);
        setValue("correo", res.data.correo);
        setValue("contraseña", res.data.contraseña);
        setValue("apodoUsuario", res.data.apodoUsuario);
        setValue("direccion", res.data.direccion);
        setValue("idRegion", res.data.idRegion);
        setValue("idcomuna", res.data.idcomuna);
        setValue("idPlan", res.data.idPlan);
        setValue("idConfigUsuario", res.data.idConfigUsuario);
      }
    }
    loadUser();
  }, []);

  return (
    <div className="max-w-xl mx-auto mt-4">
      <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="rut"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("rut", { required: true })}
        />
        {errors.rut && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="idUsuario"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("idUsuario", { required: true })}
        />
        {errors.idUsuario && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="nombreUsuario"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("nombreUsuario", { required: true })}
        />
        {errors.nombreUsuario && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="correo"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("correo", { required: true })}
        />
        {errors.correoElectronico && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="contraseña"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("contraseña", { required: true })}
        />
        {errors.contraseña && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="apodoUsuario"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("apodoUsuario", { required: true })}
        />
        {errors.apodoUsuario && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="direccion"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("direccion", { required: true })}
        />
        {errors.direccion && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="idRegion"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("idRegion", { required: true })}
        />
        {errors.idRegion && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="idcomuna"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("idcomuna", { required: true })}
        />
        {errors.idcomuna && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="idPlan"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("idPlan", { required: true })}
        />
        {errors.idPlan && <span>Falta completar este campo</span>}

        <input
          type="text"
          placeholder="idConfigUsuario"
          className="bg-white p-3 rounded-lg w-full mb-3 text-black"
          {...register("idConfigUsuario", { required: true })}
        />
        {errors.idConfigUsuario && <span>Falta completar este campo</span>}

        <button
          className="bg-indigo-500 p-3 rounded-lg block w-full mt-3"
          type="submit"
        >
          Guardar
        </button>
        {params.idUsuario && (
          <button
            className="bg-red-500 p-3 rounded-lg w-48 mt-3"
            onClick={async () => {
              const accepted = window.confirm("estas seguro?");
              if (accepted) {
                await deleteUsers(params.idUsuario);
                toast.success("Usuario Eliminado", {
                  position: "bottom-right",
                  style: {
                    background: "#101010",
                    color: "#fff",
                  },
                });
                navigate("/Crear-Usuario");
              }
            }}
          >
            Delete
          </button>
        )}
      </form>
    </div>
  );
}

export default UserFormPage;
