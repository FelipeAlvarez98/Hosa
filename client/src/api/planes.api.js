// En plans.api.js
import axios from 'axios';

export const getPlanDetails = (idPlan) => {
  return axios.get(`http://localhost:8000/BackOffice/planes/${idPlan}`);
};