export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      // Return the desired object on resolution
      return { status: 200, body: 'success' };
    })
  // Handler for when the promise rejects
    .catch(() => {
      console.log('Got a response from the API');
      // Return an empty Error object on rejection
      return (new Error());
    });
}
