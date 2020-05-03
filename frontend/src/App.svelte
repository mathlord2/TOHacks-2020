<script>
	//import { Router, Route } from "svelte-routing";
	import MainPage from "./components/mainPage.svelte";
	import Navbar from "./components/navbar.svelte";
	import Auth from "./components/auth.svelte";
	import NewUser from "./components/newUser.svelte";
	import {loggedIn, currentUser, isNew} from "./stores/user.js";

	let logged;

	const unsubscribe = loggedIn.subscribe(val => {
		logged = val;
	});
</script>

{#if logged}
	{#if $isNew}
		<NewUser/>
	{:else}
		<Navbar/>
		<MainPage/>
	{/if}
{:else}
	<Auth/>
{/if}

<style>
</style>