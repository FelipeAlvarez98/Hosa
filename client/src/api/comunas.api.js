// En communes.api.js
import axios from 'axios';

export const getComunaDetails = (idcomuna) => {
  return axios.get(`http://localhost:8000/BackOffice/comunas/${idcomuna}`);
};