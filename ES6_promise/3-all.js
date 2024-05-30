import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  // Use Promise.all to wait for both promises to resolve
  Promise.all([uploadPhoto(), createUser()])
    .then((result) => {
      console.log(`${result[0].body} ${result[1].firstName} ${result[1].lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
