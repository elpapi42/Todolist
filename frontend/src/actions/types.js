/**
 * Types used for each action to be dispatched
 *
 * Naming convention (Not mandatory but highly recommended)
 * "(Reducer type)_(Action to be used)_(Description)"
 * "TODOS_GET_TODOS"
 *
 * Actions:
 * GET: Gets and replace some information
 * UPDATE: Update some information that's already in the reducer
 * DELETE: Delete some information in the reducer
 * ...More to be added if necessary
 */

export const TODOS_GET_TODOS = "TODOS_GET_TODOS";
export const TODOS_DELETE_TODO = "TODOS_DELETE_TODO";
export const TODOS_UPDATE_TODO = "TODOS_UPDATE_TODO";
export const TODOS_ADD_TODO = "TODOS_ADD_TODO";
export const TODOS_EDIT_NEW_TODO = "TODOS_EDIT_NEW_TODO";

