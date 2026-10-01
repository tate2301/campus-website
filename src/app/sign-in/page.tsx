import type { Metadata } from "next";
import Image from "next/image";
import { SitePage } from "@/components/page";
import { Lockup } from "@/components/chrome";
import { CheckInput, FieldInput } from "@/components/forms";
import { A, Cbtn, PortalIcon, PORTAL_NAMES, sx } from "@/components/ds";
import { SW } from "@/content/copy";
import { PHOTO_ALT } from "@/content/photo-alt";
import { BLUE, CW, INK, MUTED, MX, SANS } from "@/lib/design";

/**
 * Sign in lives on the app domain (app.campus.corelith.co.zw); each school reaches it at its own address, so there is
 * no school picker. This is that screen, built static: the form posts to the app.
 */
export const metadata: Metadata = { title: "Sign in", description: SW.SIGNIN.h };

const APP = "https://app.campus.corelith.co.zw/sign-in";
const show = <button type="button" style={sx(`font:500 13px ${SANS};color:${BLUE}`)}>Show</button>;
const legal: [string, string][] = [["Privacy", "/legal/privacy"], ["Terms", "/legal/terms"], ["Support", "/support"]];

/** webpages.signin */
function Desktop() {
  const S = SW.SIGNIN;
  return (
    <>
      <div style={sx("width:640px;height:900px;box-sizing:border-box;padding:48px 120px;display:flex;flex-direction:column")}>
        <div><Lockup h={24} by={false} href="/" /></div>
        <div style={sx("flex:1;display:flex;align-items:center")}>
          <form action={APP} method="post" style={sx("width:400px")}>
            <h1 style={sx(`margin:0;font:600 34px/1.1 ${SANS};letter-spacing:-0.03em`)}>{S.h}</h1>
            <div style={sx("margin-top:32px")}><FieldInput id="si-d-user" name="user" label="Email or phone number" ph="rudo.moyo@gmail.com" w={400} autoComplete="username" required /></div>
            <div style={sx("margin-top:18px")}><FieldInput id="si-d-pw" name="password" type="password" label="Password" ph="••••••••••" w={400} autoComplete="current-password" required tail={show} /></div>
            <div style={sx("display:flex;justify-content:space-between;align-items:center;margin-top:16px")}>
              <CheckInput label="Keep me signed in on this device" name="remember" value="1" checked />
              <A href={`${APP}/forgot`} style={`font:500 14px ${SANS};color:${BLUE}`}>Forgot password?</A>
            </div>
            <div style={sx("display:flex;margin-top:26px")}><Cbtn label="Sign in" icon="arrow-right-line" kind="primary" size="lg" type="submit" full /></div>
          </form>
        </div>
        <div style={sx(`display:flex;gap:20px;font:400 13px ${SANS};color:${MUTED}`)}>
          {legal.map(([t, h]) => <A key={t} href={h}>{t}</A>)}<span style={sx("margin-left:auto")}>© 2026 Corelith Labs</span>
        </div>
      </div>
      <div style={sx("position:relative;flex:1;height:900px;padding:24px 24px 24px 0;box-sizing:border-box")}>
        <div style={sx("position:relative;width:100%;height:100%;border-radius:28px;overflow:hidden")}>
          <Image src="/assets/photos/boys-reading-2.jpg" alt={PHOTO_ALT["boys-reading-2.jpg"]} width={776} height={852} loading="eager" decoding="sync"
            style={sx("width:100%;height:100%;object-fit:cover;object-position:47% 42%")} />
          <div style={sx("position:absolute;left:24px;bottom:24px;display:flex;gap:8px")}>
            {PORTAL_NAMES.map((n) => (
              <span key={n} style={sx(`display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px 0 5px;border-radius:18px;background:rgba(255,255,255,.94);font:500 13.5px ${SANS};color:${INK}`)}>
                <PortalIcon n={n} s={26} />{n}
              </span>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

/** mobile.signin */
function Phone() {
  const S = SW.SIGNIN;
  return (
    <>
      <div style={sx("position:relative;height:250px")}>
        <Image src="/assets/photos/boys-reading-2.jpg" alt={PHOTO_ALT["boys-reading-2.jpg"]} width={390} height={250} loading="eager" decoding="sync"
          style={sx("width:100%;height:100%;object-fit:cover;object-position:47% 42%")} />
        <div style={sx(`position:absolute;left:${MX}px;right:${MX}px;bottom:14px;display:flex;flex-wrap:wrap;gap:6px`)}>
          {PORTAL_NAMES.map((n) => (
            <span key={n} style={sx(`display:inline-flex;align-items:center;gap:5px;height:30px;padding:0 10px 0 4px;border-radius:15px;background:rgba(255,255,255,.94);font:500 12.5px ${SANS}`)}>
              <PortalIcon n={n} s={22} />{n}
            </span>
          ))}
        </div>
      </div>
      <form action={APP} method="post" style={sx(`padding:28px ${MX}px`)}>
        <Lockup h={22} by={false} href="/" />
        <h1 style={sx(`margin:22px 0 0;font:600 30px/1.1 ${SANS};letter-spacing:-0.03em`)}>{S.h}</h1>
        <div style={sx("margin-top:24px")}><FieldInput id="si-p-user" name="user" label="Email or phone number" ph="rudo.moyo@gmail.com" w={CW} autoComplete="username" required /></div>
        <div style={sx("margin-top:16px")}><FieldInput id="si-p-pw" name="password" type="password" label="Password" ph="••••••••••" w={CW} autoComplete="current-password" required tail={show} /></div>
        <div style={sx("display:flex;justify-content:space-between;align-items:center;margin-top:14px")}>
          <CheckInput label="Keep me signed in" name="remember" value="1" checked />
          <A href={`${APP}/forgot`} style={`font:500 14px ${SANS};color:${BLUE}`}>Forgot password?</A>
        </div>
        <div style={sx("margin-top:22px")}><div style={sx("display:flex")}><Cbtn label="Sign in" icon="arrow-right-line" kind="primary" size="lg" type="submit" full /></div></div>
      </form>
      <div style={sx(`position:absolute;left:${MX}px;right:${MX}px;bottom:24px;display:flex;gap:18px;font:400 13px ${SANS};color:${MUTED}`)}>
        {legal.map(([t, h]) => <A key={t} href={h}>{t}</A>)}
      </div>
    </>
  );
}

export default function SignIn() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} desktopStyle="min-height:900px;display:flex" phoneStyle="height:844px;position:relative" />;
}
