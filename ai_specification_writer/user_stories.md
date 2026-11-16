# User Stories: CarpoolConnect

### User Story 1
As a corporate commuter, I want to register and log in using my company email or SSO so that I only share rides with verified colleagues from my organization.

**Acceptance Criteria**:
- User can authenticate using corporate SSO (Google Workspace, Microsoft Entra ID) or verify via a corporate email domain OTP.
- Unverified personal email domains (e.g., `@gmail.com`) are rejected during onboarding.
- User profile automatically displays their verified company name and office campus.

**Priority**: MVP

---

### User Story 2
As a driver, I want to publish my recurring daily commute route and schedule so that colleagues along my path can request to join my ride.

**Acceptance Criteria**:
- Driver can set origin address, destination office campus, departure time, and active days of the week.
- Driver can specify available seat count (1–4) and maximum detour tolerance (e.g., 5–15 minutes).
- Published route appears in search results for matching passengers within 5 seconds.

**Priority**: MVP

---

### User Story 3
As a passenger, I want to search for available drivers along my commute route and schedule so that I can find a reliable ride to the office.

**Acceptance Criteria**:
- Passenger enters home pickup point, target office location, and desired arrival window.
- System displays matching drivers sorted by route overlap, departure time proximity, and driver rating.
- Search results display estimated pickup time, detour impact, and cost contribution before booking.

**Priority**: MVP

---

### User Story 4
As a passenger, I want to request a seat on a driver's commute and receive confirmation so that my ride is guaranteed in advance.

**Acceptance Criteria**:
- Passenger can submit a ride request for a single trip or recurring weekly schedule in under 3 clicks.
- Driver receives an instant push/in-app notification and can accept or decline the request.
- Once accepted, seat availability decrements automatically and both users receive calendar/trip reminders.

**Priority**: MVP

---

### User Story 5
As a commuter (driver or passenger), I want to view live trip status and use in-app messaging so that we can coordinate exact pickup spots without sharing personal phone numbers.

**Acceptance Criteria**:
- Users can exchange pre-set quick messages (e.g., "I'm outside", "Running 3 mins late") or custom text within an active trip thread.
- Passenger can view the driver's real-time location and updated ETA starting 15 minutes before pickup.
- Chat history is automatically archived 24 hours after trip completion for privacy.

**Priority**: High

---

### User Story 6
As a passenger, I want to automatically split fuel and toll costs through the app so that I avoid awkward cash exchanges with coworkers.

**Acceptance Criteria**:
- System calculates a transparent per-seat cost share based on trip distance and local fuel/mileage rates.
- Passenger's linked payment method or corporate commuter stipend is charged automatically upon trip completion.
- Driver receives payout or wallet credit with a downloadable trip receipt.

**Priority**: High

---

### User Story 7
As a commuter, I want to rate my co-riders and leave feedback after a trip so that the platform maintains a trustworthy and punctual community.

**Acceptance Criteria**:
- Both driver and passenger are prompted to submit a 1–5 star rating and optional tags (e.g., "Punctual", "Great conversation") after trip completion.
- User's aggregate rating updates on their public profile after at least 3 completed trips.
- Users can block or report safety/conduct issues directly from the post-trip screen.

**Priority**: High

---

### User Story 8
As a driver, I want to unlock priority corporate parking passes when I carpool with colleagues so that I am incentivized to share empty seats.

**Acceptance Criteria**:
- System verifies multi-occupancy arrival at the office campus via GPS check-in or QR scan.
- Qualified carpools automatically generate a digital priority parking pass for that workday.
- Facility administrators can configure minimum passenger requirements (e.g., 2+ employees per vehicle) per campus.

**Priority**: Medium

---

### User Story 9
As a corporate sustainability manager, I want to view an ESG and commute analytics dashboard so that I can track CO₂ reductions and single-occupancy vehicle (SOV) trips avoided.

**Acceptance Criteria**:
- Dashboard displays total trips shared, miles reduced, estimated kg of CO₂ saved, and active employee participation rate.
- Data can be filtered by date range, department, and office location.
- Admin can export summary reports in CSV and PDF formats for quarterly ESG disclosures.

**Priority**: Medium

---

### User Story 10
As a frequent commuter, I want to form a saved "Carpool Pod" with trusted coworkers so that we can rotate driving duties effortlessly each week.

**Acceptance Criteria**:
- Users can invite up to 4 verified colleagues into a private recurring Carpool Pod.
- Pod members can assign who drives on specific days of the week on a shared calendar.
- Automated reminders notify the designated driver and passengers the evening before each scheduled commute.

**Priority**: Low
