%define tarball xf86-video-glint
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

# FIXME: DRI support for glint is more or less nonfunctional and unlikely to
# ever be fixed.
%define with_dri        1

Summary:   Xorg X11 glint video driver
Name:      xorg-x11-drv-glint
Version:   1.2.4
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   glint.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-devel >= 1.6.0
%if %{with_dri}
BuildRequires: mesa-libGL-devel >= 6.4-4
BuildRequires: libdrm-devel >= 2.0-1
%endif

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.6.0

%description 
X.Org X11 glint video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static \
%if ! %{with_dri}
           --disable-dri
%endif
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/glint_drv.so
%{_datadir}/hwdata/videoaliases/glint.xinf
%{_mandir}/man4/glint.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.4-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.2.4-1
- glint 1.2.4

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.2.3-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.2.3-1
- glint 1.2.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.2.2-1
- Latest upstream release

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.2.0-1
- Latest upstream release

* Tue Mar 11 2008 Dave Airlie <airlied@gmail.com> 1.1.1-9
- pciaccess conversion

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.1-8
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.1.1-7
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.1-6
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.1.1-5
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 1.1.1-4
- Re-enable with_dri, as --disable-dri builds are broken (fdo#7405)

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 1.1.1-3
- Added with_dri conditionalization, defaulted to DRI being disabled.
- Added "BuildRequires: libdrm-devel >= 2.0-1" for (#192358).
- Added "BuildRequires: mesa-libGL-devel >= 6.4-4".
- Bumped sdk dep to pick up proto-devel indirectly.

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.1.1-1
- Update to 1.1.1 from 7.1RC1.

* Wed Feb 22 2006 Mike A. Harris <mharris@redhat.com> 1.0.1.3-2
- Install glint.xinf, which was inadvertently left out of packaging (#182502)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1.3-1
- Updated xorg-x11-drv-glint to version 1.0.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.1.2-1
- Updated xorg-x11-drv-glint to version 1.0.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated xorg-x11-drv-glint to version 1.0.1 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-glint to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to i386, alpha

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for glint video driver generated automatically
  by my xorg-driverspecgen script.
