import axios from "axios";
import Cookies from "js-cookie";

import { CSRF_CONFIG } from "../config";

const CSRF_USE_SESSIONS = CSRF_CONFIG.useSessions;
const SPA_CROSS_SITE = CSRF_CONFIG.crossSite;
const CSRF_TOKEN_IN_RESPONSE_BODY = SPA_CROSS_SITE || CSRF_USE_SESSIONS;

const api = axios.create({
  baseURL: CSRF_CONFIG.baseUrl,
  withCredentials: true,
});

// Stores the most recent CSRF token.
let MOST_RECENT_RESPONSE_CSRF_TOKEN = "";

// A request interceptor runs before each request
api.interceptors.request.use(async (config) => {
  if (
    ["PATCH", "POST", "PUT", "DELETE"].includes(config.method.toUpperCase())
  ) {
    config.headers["X-CSRFToken"] = CSRF_TOKEN_IN_RESPONSE_BODY
      ? MOST_RECENT_RESPONSE_CSRF_TOKEN
      : Cookies.get("csrftoken");
  }

  return config;
});

// Authentication Requests
/**
 * Extracts the CSRF token from a response, if available, and sets the MOST_RECENT_RESPONSE_CSRF_TOKEN variable to
 * the extracted value.
 */
async function csrfTokenExtractionHandler(requestPromise) {
  const response = await requestPromise;

  if (CSRF_TOKEN_IN_RESPONSE_BODY && response.data.csrf) {
    MOST_RECENT_RESPONSE_CSRF_TOKEN = response.data.csrf;
  }

  return response;
}

export function login(username, password) {
  return csrfTokenExtractionHandler(
    api.post("/accounts/login/", { username, password })
  );
}

export function logout() {
  return csrfTokenExtractionHandler(api.post("/accounts/logout/"));
}

export async function getUserAccount() {
  const response = await csrfTokenExtractionHandler(api.get("/accounts/me/"));

  // Just because of the different scenarios. You don't need that in practice.
  if (CSRF_TOKEN_IN_RESPONSE_BODY) {
    return response.data.user;
  } else {
    return response.data;
  }
}

// Application Requests

export function getReminders() {
  return api.get("/reminders/");
}

export default api;
