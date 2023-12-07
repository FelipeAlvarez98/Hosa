// En regions.api.js
import axios from 'axios';

export const getRegionDetails = (idRegion) => {
  return axios.get(`http://localhost:8000/BackOffice/regiones/${idRegion}`);
};