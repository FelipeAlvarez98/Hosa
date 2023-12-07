import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { UserPage } from "./pages/UserPage";
import { UserFormPage } from "./pages/UserFormPage";
import { Navigation } from "./components/Navigation";
import { Toaster } from "react-hot-toast";
import { Dispositivosv1Page } from "./pages/Dispositivosv1Page";

function App() {
  return (
    <BrowserRouter>
      <div className="w-full mx-auto place-content-center">
        <Navigation />
        <Routes>
          <Route path="/" element={<Navigate to={"/BackOffice"} />} />
          <Route path="/Usuario" element={<UserPage />} />
          <Route path="/Crear-Usuario" element={<UserFormPage />} />
          <Route path="/Crear-Usuario/:idUsuario" element={<UserFormPage />} />
          <Route path="/DispositivosV1" element={<Dispositivosv1Page />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
