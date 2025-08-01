##  1. **S – Spoofing Identity**

> Pretending to be someone else.
> 

###  Where it happens

- Uploading a file with another user’s identity
- Manually sending API requests with fake user ID
- Using someone else’s JWT token

###  Mitigations

| Area | Fix |
| --- | --- |
| API | Use **JWT** for authentication |
| Backend | Never trust client-side `user_id`, always extract from **token** |
| Storage | Bind files to server-verified user identity |
| Admin Access | Use role-based verification (`is_admin`) on sensitive routes |

---

##  2. **T – Tampering**

> Unauthorized modification of files, data, or metadata.
> 

###  Where it happens

- Changing file content in transit
- Modifying metadata before/after upload
- Manipulating cleanup strategy logic or file ID

###  Mitigations

| Area | Fix |
| --- | --- |
| Upload | Use **HTTPS** to protect data in transit |
| Metadata | Regenerate metadata **server-side only** (via Visitor pattern) |
| Files | Use **hashes (SHA256)** to verify integrity |
| Cleanup | Do not expose file IDs or strategy internals to users |

---

##  3. **R – Repudiation**

> User denies performing an action, and there's no evidence.
> 

###  Where it happens

- User claims “I didn’t upload that file”
- Admin says “I never deleted anything”
- No logs of cleanup actions

###  Mitigations

| Area | Fix |
| --- | --- |
| Upload/Delete | Log all actions: user, file ID, timestamp, action |
| Cleanup | Store **cleanup logs** per file with strategy name |
| Download | Log download events for accountability |
| Admin | Tag all privileged actions with `admin_id` and endpoint used |
| Logging | Store logs in **append-only files** or log servers |

---

##  4. **I – Information Disclosure**

> Unauthorized access to sensitive data.
> 

###  Where it happens

- User accesses another user’s file
- Public S3 bucket exposes media files
- Metadata leaks EXIF/GPS info

###  Mitigations

| Area | Fix |
| --- | --- |
| File Access | Always validate file **ownership** before returning it |
| S3 | Make buckets **private**, use **signed URLs** |
| Metadata | Sanitize metadata (remove EXIF/GPS if needed) |
| Logging | Don’t log secrets or file paths that reveal user info |
| Admin API | Protect endpoints with strict auth & roles |

---

##  5. **D – Denial of Service**

> Disrupting the system so others can’t use it.
> 

###  Where it happens

- Uploading huge files repeatedly
- Repeated cleanup requests
- Uploading malformed files to crash metadata visitors

###  Mitigations

| Area | Fix |
| --- | --- |
| Upload | Set **max file size**, limit file types |
| API | Apply **rate limiting** (e.g. 10 uploads/min/user) |
| Visitor | Use `try/except` and **timeouts** during metadata extraction |
| Cleanup | Limit file deletions per call (`max=5`) and rate-limit endpoint |
| Infrastructure | Use **gunicorn workers**, Cloudflare, or API Gateway for request filtering |

---

##  6. **E – Elevation of Privilege**

> User gains access to actions/data they shouldn’t.
> 

###  Where it happens

- Regular user deletes other users’ files
- User triggers `POST /cleanup/` (admin-only)
- Uploads a file on behalf of another

###  Mitigations

| Area | Fix |
| --- | --- |
| RBAC | Define roles (`user`, `admin`) and enforce them at each endpoint |
| Ownership | Verify **file.owner_id == request.user.id** |
| Admin APIs | Restrict by role inside JWT claims |
| Input Validation | Never allow client to set `user_id`, `strategy`, etc. |