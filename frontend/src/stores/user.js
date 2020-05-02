import {writable} from "svelte/store";

export const currentUser = writable(null);
export const isNew = writable(null);
export const userType = writable("Doctor"); //"Doctor" or "Patient"