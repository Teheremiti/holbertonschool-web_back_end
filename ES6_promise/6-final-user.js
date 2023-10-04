import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      const promises = [];
      results.forEach((promise) => {
        promises.push({
          status: promise.status,
          value: promise.value,
        });
      });
      return promises;
    })
}
