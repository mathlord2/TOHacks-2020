<script>
    import {onMount} from 'svelte';
    import {currentUser} from "./../stores/user.js";

    onMount(() => {
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                // User is signed in.
                var displayName = user.displayName;
                var email = user.email;
                var uid = user.uid;
                currentUser.set(user);
            } else {
                currentUser.set(null);
            }
        }, function(error) {
            console.log(error);
        });
    });
</script>