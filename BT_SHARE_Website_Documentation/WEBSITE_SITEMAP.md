# Website Sitemap & Angular Route Plan

**Public routes** (final slugs subject to design):

| Route | Page | Content |
|---|---|---|
| `/` | Home | Value proposition, verified status, featured products/apps |
| `/products` | Products | All hardware and software offerings |
| `/products/:slug` | Product detail | Capabilities, status, specifications, related docs |
| `/apps` | Applications | Software application catalogue |
| `/apps/:slug` | Application detail | Description, images, versions and links |
| `/docs` | Documentation index | Categories and search |
| `/docs/:product/:version/:slug` | Documentation article | Approved article and version |
| `/downloads` | Android Downloads | Published APK releases |
| `/downloads/:app` | Application releases | Latest and historic versions |
| `/downloads/:app/:version` | Release detail | Notes, SHA-256, requirements, verified download |
| `/about` | About | Approved company narrative |
| `/contact` | Contact | Approved support channels |
| `/privacy` | Privacy | Required before personal data collection |
| `/404` | Not found | Safe fallback |

**Admin routes:**

| Route | Page |
|---|---|
| `/admin/login` | Sign in using selected identity service; must not bypass MFA |
| `/admin` | Overview / actionable alerts |
| `/admin/products` | Product catalogue management |
| `/admin/apps` | Application catalogue management |
| `/admin/docs` | Documentation workbench |
| `/admin/releases` | APK release workbench |
| `/admin/media` | Media assets |
| `/admin/content` | Website page content |
| `/admin/users` | Admin invitations and role assignments (owner role) |
| `/admin/audit` | Audit search (authorized roles) |

Route guards improve UX only. **Security is enforced by authenticated backend API requests on every read/write**; all admin SSR caches and public search indexes must avoid private content.
