<script>
	//import { Router, Route } from "svelte-routing";
	import MainPage from "./components/mainPage.svelte";
	import Navbar from "./components/navbar.svelte";
	import Auth from "./components/auth.svelte";
	import NewUser from "./components/newUser.svelte";
	import {currentUser, isNew} from "./stores/user.js";
</script>

{#if $currentUser}
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