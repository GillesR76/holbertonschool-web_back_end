import signUpUser from './4-user-promise';
import { uploadPhoto } from './utils';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => results.map(({ status, value, error }) => ({
      status,
      value: status === 'fulfilled' ? value : error,
    })));
}
