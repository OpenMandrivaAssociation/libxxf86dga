%define libxxf86dga %mklibname xxf86dga 1
Name: libxxf86dga
Summary:  XFree86 Direct Graphics Access Extension Library
Version: 1.0.1
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Direct Graphics Access Extension Library

#-----------------------------------------------------------

%package -n %{libxxf86dga}
Summary:  XFree86 Direct Graphics Access Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Conflicts: XFree86-compat-libs <= 4.1.0
Provides: %{name} = %{version}

%description -n %{libxxf86dga}
 XFree86 Direct Graphics Access Extension Library

#-----------------------------------------------------------

%package -n %{libxxf86dga}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxxf86dga} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxxf86dga-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxxf86dga}-devel
Development files for %{name}

%files -n %{libxxf86dga}-devel
%defattr(-,root,root)
%{_libdir}/libXxf86dga.so
%{_libdir}/libXxf86dga.la
%{_libdir}/pkgconfig/xxf86dga.pc
%{_mandir}/man3/XDGA*.3x.bz2
%{_mandir}/man3/XF86DGA.3x.bz2
%{_mandir}/man3/XFree86-DGA.3x.bz2

#-----------------------------------------------------------

%package -n %{libxxf86dga}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxxf86dga}-devel = %{version}
Provides: libxxf86dga-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxxf86dga}-static-devel
Static development files for %{name}

%files -n %{libxxf86dga}-static-devel
%defattr(-,root,root)
%{_libdir}/libXxf86dga.a

#-----------------------------------------------------------

%prep
%setup -q -n libXxf86dga-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxxf86dga}
%defattr(-,root,root)
%{_libdir}/libXxf86dga.so.1
%{_libdir}/libXxf86dga.so.1.0.0


