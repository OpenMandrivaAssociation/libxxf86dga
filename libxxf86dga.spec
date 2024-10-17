%define major 1
%define libname %mklibname xxf86dga %{major}
%define devname %mklibname xxf86dga -d

Summary:	XFree86 Direct Graphics Access Extension Library
Name:		libxxf86dga
Version:	1.1.6
Release:	2
License:	MIT
Group:		Development/X11
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto)

%description
XFree86 Direct Graphics Access Extension Library.

%package -n %{libname}
Summary:	XFree86 Direct Graphics Access Extension Library
Group:		Development/X11

%description -n %{libname}
XFree86 Direct Graphics Access Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libXxf86dga-%{version} -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libXxf86dga.so.%{major}*

%files -n %{devname}
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_includedir}/X11/extensions/*.h
%doc %{_mandir}/man3/XDGA*.3*
%doc %{_mandir}/man3/XF86DGA.3*
%doc %{_mandir}/man3/XFree86-DGA.3*
