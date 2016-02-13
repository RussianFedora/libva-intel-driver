Name:           libva-intel-driver
Version:        1.6.2
Release:        1%{?dist}
Summary:        HW video decode support for Intel graphics

License:        MIT and ASL 2.0
URL:            https://cgit.freedesktop.org/vaapi/intel-driver
Source0:        https://www.freedesktop.org/software/vaapi/releases/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  /usr/bin/python2
BuildRequires:  /usr/bin/m4
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(intel-gen4asm)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
# X11
BuildRequires:  pkgconfig(libva-x11)
# Wayland
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libva-wayland)

%description
%{summary}.

%prep
%autosetup

%build
%configure --enable-drm --enable-x11 --enable-wayland
%make_build V=1

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete

%files
%license COPYING
%doc README NEWS
%{_libdir}/dri/i965_drv_video.so

%changelog
* Sat Feb 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.6.2-1
- Initial package
