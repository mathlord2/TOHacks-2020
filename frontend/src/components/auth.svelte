<script>
    import {onMount} from 'svelte';
    import {currentUser, userId, userType, isNew, condition} from './../stores/user.js';

    onMount(() => {
        var uiConfig = {
            signInOptions: [
                // Leave the lines as is for the providers you want to offer your users.
                firebase.auth.GoogleAuthProvider.PROVIDER_ID,
                firebase.auth.EmailAuthProvider.PROVIDER_ID,
            ],
            // tosUrl and privacyPolicyUrl accept either url string or a callback
            // function.
            // Terms of service url/callback.
            callbacks: {
                signInSuccessWithAuthResult: function(authResult, redirectUrl) {
                    var user = authResult.user;
                    var isNewUser = authResult.additionalUserInfo.isNewUser;
                    currentUser.set(user);
                    userId.set(user.email);
                    isNew.set(isNewUser);
                    getUserData();
                    return true;
                },
                signInFailure: function(error) {
                    // Some unrecoverable error occurred during sign-in.
                    // Return a promise when error handling is completed and FirebaseUI
                    // will reset, clearing any UI. This commonly occurs for error code
                    // 'firebaseui/anonymous-upgrade-merge-conflict' when merge conflict
                    // occurs. Check below for more details on this.
                    return handleUIError(error);
                },
            }
        };

        // Initialize the FirebaseUI Widget using Firebase.
        var ui = firebaseui.auth.AuthUI.getInstance() || new firebaseui.auth.AuthUI(firebase.auth());
        // The start method will wait until the DOM is loaded.
        ui.start('#firebaseui-auth-container', uiConfig);
    });

    let id;

    const unsubscribe = userId.subscribe(val => {
        id = val;
    })

    function getUserData() {
        db.collection("users").get().then(function(querySnapshot) {
            querySnapshot.forEach(function(doc) {
                // doc.data() is never undefined for query doc snapshots
                if (id == doc.data().idUser) {
                    userType.set(doc.data().type);
                    if (doc.data().type == "Patient") {
                        condition.set(doc.data().condition);
                    }
                }
            });
        });
    }
</script>

<h1 align="center">Welcome to Cov-Vision</h1>
<div id="firebaseui-auth-container"></div>

<style>
    h1 {
        margin-top: 40px;
        font-size: 40px;
    }

    #firebaseui-auth-container {
        margin-top: 10%;
    }
</style>