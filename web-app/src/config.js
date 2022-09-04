// TODO: Change this to the scenario you want to try out. Check out the global README.md for more information.
// Possible Values: 1, 2, 3, 4, 5, 6; Other values for manual configuration
const USED_CSRF_SCENARIO = 1;

export const CSRF_CONFIG = {};
switch (USED_CSRF_SCENARIO) {
  // Localhost, same-site, cross-origin
  case 1: // Double Submit Cookie
    CSRF_CONFIG.useSessions = false;
    CSRF_CONFIG.crossSite = false;
    CSRF_CONFIG.baseUrl = "http://localhost:8000";
    break;
  case 2: // Synchronizer Token Pattern
    CSRF_CONFIG.useSessions = true;
    CSRF_CONFIG.crossSite = false;
    CSRF_CONFIG.baseUrl = "http://localhost:8000";
    break;

  // *.example.org, same-site, cross-origin
  // Requires adding the following to your /etc/hosts file:
  // 127.0.0.1 api.example.org
  // 127.0.0.1 web.example.org
  case 3: // Double Submit Cookie
    CSRF_CONFIG.useSessions = false;
    CSRF_CONFIG.crossSite = false;
    CSRF_CONFIG.baseUrl = "http://api.example.org:8000";
    break;
  case 4: // Synchronizer Token Pattern
    CSRF_CONFIG.useSessions = true;
    CSRF_CONFIG.crossSite = false;
    CSRF_CONFIG.baseUrl = "http://api.example.org:8000";
    break;

  // api.example.org, myfrontend.com, cross-site,
  // Requires adding the following to your /etc/hosts file:
  // 127.0.0.1 api.example.org
  // 127.0.0.1 myfrontend.com
  case 5: // Double Submit Cookie
    CSRF_CONFIG.useSessions = false;
    CSRF_CONFIG.crossSite = true;
    CSRF_CONFIG.baseUrl = "http://api.example.org:8000";
    break;
  case 6: // Synchronizer Token Pattern
    CSRF_CONFIG.useSessions = true;
    CSRF_CONFIG.crossSite = true;
    CSRF_CONFIG.baseUrl = "http://api.example.org:8000";
    break;
  default:
    // Up to you to configure
    CSRF_CONFIG.useSessions = false;
    CSRF_CONFIG.crossSite = false;
    CSRF_CONFIG.baseUrl = "http://localhost:8000";
    break;
}
